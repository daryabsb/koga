"""
BROTHER PRINTER STUFF
"""
import sys
import logging
import json
import argparse
# import qrcode

from PIL import Image, ImageDraw, ImageFont

from brother_ql.devicedependent import label_type_specs, label_sizes
from brother_ql.devicedependent import ENDLESS_LABEL, DIE_CUT_LABEL, ROUND_DIE_CUT_LABEL
from brother_ql import BrotherQLRaster, create_label
from brother_ql.backends import backend_factory, guess_backend

# CONTEXT

logger = logging.getLogger(__name__)




def get_label_context(request):
    """ might raise LookupError() """

    d = request.values  # UTF-8 decoded form data

    context = {
        'text':          d.get('text', None),
        'font_size': int(d.get('font_size', 100)),
        'font_family':   d.get('font_family'),
        'font_style':    d.get('font_style'),
        'label_size':    d.get('label_size', "62"),
        'kind':          label_type_specs[d.get('label_size', "62")]['kind'],
        'margin':    int(d.get('margin', 10)),
        'threshold': int(d.get('threshold', 70)),
        'align':         d.get('align', 'center'),
        'orientation':   d.get('orientation', 'standard'),
        'margin_top':    float(d.get('margin_top',    24))/100.,
        'margin_bottom': float(d.get('margin_bottom', 45))/100.,
        'margin_left':   float(d.get('margin_left',   35))/100.,
        'margin_right':  float(d.get('margin_right',  35))/100.,
        'print_type':    d.get('print_type', 'text'),
        'qrcode_size':   int(d.get('qrcode_size', 10)),
        'qrcode_correction': d.get('qrcode_correction', 'L'),
        'print_count':       int(d.get('print_count', 1)),
        'print_color':       d.get('print_color', 'black'),
        'line_spacing':      int(d.get('line_spacing', 100)),
        'cut_once':          int(d.get('cut_once', 0)),
    }
    context['margin_top']    = int(context['font_size']*context['margin_top'])
    context['margin_bottom'] = int(context['font_size']*context['margin_bottom'])
    context['margin_left']   = int(context['font_size']*context['margin_left'])
    context['margin_right']  = int(context['font_size']*context['margin_right'])

    context['fill_color']    = (255, 0, 0) if 'red' in context['label_size'] and context['print_color'] == 'red' else (0, 0, 0)

    context['cut_once'] = True if context['cut_once'] == 1 else False

# ########



LABEL_SIZES = [(
    name,
    label_type_specs[name]['name'],
    (label_type_specs[name]['kind'] in (
        ROUND_DIE_CUT_LABEL,))  # True if round label
) for name in label_sizes]

LINE_SPACINGS = (100, 150, 200, 250, 300)

# Don't change as brother_ql is using this DPI value
DEFAULT_DPI = 300

try:
    with open('config.json', encoding='utf-8') as fh:
        CONFIG = json.load(fh)
        print('CONFIG IS OPEN')
        print(CONFIG)
except FileNotFoundError as e:
    with open('config.example.json', encoding='utf-8') as fh:
        print('CONFIG NOT OPEN')
        CONFIG = json.load(fh)

selected_backend = guess_backend(CONFIG['PRINTER']['PRINTER'])
BACKEND_CLASS = backend_factory(selected_backend)['backend_class']


def print_text(file):
    """
    API to print a label
    returns: JSON
    Ideas for additional URL parameters:
    - alignment
    """

    return_dict = {'success': False}

    # try:
    #     context = get_label_context(request)
    # except LookupError as e:
    #     return_dict['error'] = e.msg
    #     return return_dict

    # if context['text'] is None:
    #     return_dict['error'] = 'Please provide the text for the label'
    #     return return_dict

    # im = create_label_im(**context)
    # if DEBUG:
    #     im.save('sample-out.png')

    # if context['kind'] == ENDLESS_LABEL:
    #     rotate = 0 if context['orientation'] == 'standard' else 90
    # elif context['kind'] in (ROUND_DIE_CUT_LABEL, DIE_CUT_LABEL):
    #     rotate = 'auto'
    # get_label_context()

    qlr = BrotherQLRaster(CONFIG['PRINTER']['PRINTER'])
    print(qlr.model)
    red = False
    # if 'red' in context['label_size']:
    #     red = True

    # for cnt in range(1, context['print_count']+1):
    #     if context['cut_once'] == False:
    #         cut = True
    #     elif context['cut_once'] == True and cnt == context['print_count']:
    #         cut = True
    #     else:
    #         cut = False

    create_label(
        qlr,
        file,
        "62"
        
        )
            # context['label_size'],
            # red=red,
            # threshold=context['threshold'],
            # cut=cut,
            # rotate=rotate
            

    # if not DEBUG:
    try:
        be = BACKEND_CLASS(CONFIG['PRINTER']['PRINTER'])
        be.write(qlr.data)
        be.dispose()
        del be
    except Exception as e:
        return_dict['message'] = str(e)
        logger.warning('Exception happened: %s', e)
        return return_dict

    return_dict['success'] = True
    # if DEBUG:
    return_dict['data'] = str(qlr.data)
    return return_dict
# END BROTHER