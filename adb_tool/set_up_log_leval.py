# # # -*- coding: utf-8 -*-
# import os
# import re
# import logging
# from logging import handlers
# import time
#
#
# def check_device_type():
#     # 获取当前所有连接的adb设备
#     def check_current_adb():
#         device_list = []
#         device_re = r'(.*)	device'
#         command = 'adb devices'
#         r = os.popen(command)
#         info = r.readlines()
#         for line in info:
#             line = line.strip('\r\n')
#             search_result = re.match(device_re, line, re.M | re.I)
#             if search_result:
#                 device_list.append(search_result.group(1))
#         return device_list
#
#     # 设备信息保存字典中
#     device_type_dict = {'x_front_8155': '', 'x_rear_8155': '', 'phone': '', 'm01': ''}
#     for i in range(0, len(check_current_adb())):
#         # 如果设备名称以f或者r结尾，则为x01的前或后8155设备
#         if 'f' == check_current_adb()[i][-1]:
#             device_type_dict['x_front_8155'] = check_current_adb()[i]
#         elif 'r' == check_current_adb()[i][-1]:
#             device_type_dict['x_rear_8155'] = check_current_adb()[i]
#         # 除此之外的设备，名称长度大于8的认为是手机设备，长度等于8的认为m01设备
#         else:
#             if len(check_current_adb()[i]) > 8:
#                 device_type_dict['phone'] = check_current_adb()[i]
#             if len(check_current_adb()[i]) == 8:
#                 device_type_dict['m01'] = check_current_adb()[i]
#     logging.info('flash_all_build: check_device_type: all device id is ' + str(device_type_dict))
#     return device_type_dict
# def runcmd(device_id):
#     os.system('adb -s ' + device_id + ' root')
#     time.sleep(1)
#     os.system('adb -s ' + device_id + ' shell')
#     time.sleep(1)
#     os.system('adb -s ' + device_id + ' shell setprop persist.log.tag F ')
#     time.sleep(1)
#     os.system('adb -s ' + device_id + ' shell setprop persist.log.tag.ttsService D ')
#     # if device_id[-1] == "r":
#     #     log.logger.info('flash_all_build: runcmd: ' + device_id +
#     #                     ' shell ')
#     #     os.system('adb -s ' + device_id + ' shell setprop persist.log.tag F ')
#     # else:
#     #     log.logger.info('flash_all_build: flash_5g: ' + device_id +
#     #                     '  ')
#     #     os.system('adb -s ' + device_id + ' shell QFirehose -f /data/modemfw')
#
#
# if __name__ == '__main__':
#     # try:
#     #     device_info_dict = check_device_type()


# !/usr/bin/env python
"""
    Example of (almost) all Elements, that you can use in PySimpleGUI.
    Shows you the basics including:
        Naming convention for keys
        Menubar format
        Right click menu format
        Table format
        Running an async event loop
        Theming your application (requires a window restart)
        Displays the values dictionary entry for each element
        And more!

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg


def make_window(theme):
    sg.theme(theme)
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']]]
    right_click_menu_def = [[], ['Nothing', 'More Nothing', 'Exit']]

    # Table Data
    data = [["John", 10], ["Jen", 5]]
    headings = ["Name", "Score"]

    input_layout = [[sg.Menu(menu_def, key='-MENU-')],
                    [sg.Text('Anything that requires user-input is in this tab!')],
                    [sg.Input(key='-INPUT-')],
                    [sg.Slider(orientation='h', key='-SKIDER-'),
                     sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='-GIF-IMAGE-'), ],
                    [sg.Checkbox('Checkbox', default=True, k='-CB-')],
                    [sg.Radio('Radio1', "RadioDemo", default=True, size=(10, 1), k='-R1-'),
                     sg.Radio('Radio2', "RadioDemo", default=True, size=(10, 1), k='-R2-')],
                    [sg.Combo(values=('Combo 1', 'Combo 2', 'Combo 3'), default_value='Combo 1', readonly=True,
                              k='-COMBO-'),
                     sg.OptionMenu(values=('Option 1', 'Option 2', 'Option 3'), k='-OPTION MENU-'), ],
                    [sg.Spin([i for i in range(1, 11)], initial_value=10, k='-SPIN-'), sg.Text('Spin')],
                    [sg.Multiline(
                        'Demo of a Multi-Line Text Element!\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nYou get the point.',
                        size=(45, 5), k='-MLINE-')],
                    [sg.Button('Button'), sg.Button('Popup'),
                     sg.Button(image_data=sg.DEFAULT_BASE64_ICON, key='-LOGO-')]]

    asthetic_layout = [[sg.T('Anything that you would use for asthetics is in this tab!')],
                       [sg.Image(data=sg.DEFAULT_BASE64_ICON, k='-IMAGE-')],
                       [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='-PROGRESS BAR-'),
                        sg.Button('Test Progress bar')]]

    logging_layout = [[sg.Text("Anything printed will display here!")], [sg.Output(size=(60, 15), font='Courier 8')]]

    graphing_layout = [[sg.Text("Anything you would use to graph will display here!")],
                       [sg.Graph((200, 200), (0, 0), (200, 200), background_color="black", key='-GRAPH-',
                                 enable_events=True)],
                       [sg.T('Click anywhere on graph to draw a circle')],
                       [sg.Table(values=data, headings=headings, max_col_width=25,
                                 background_color='black',
                                 auto_size_columns=True,
                                 display_row_numbers=True,
                                 justification='right',
                                 num_rows=2,
                                 alternating_row_color='black',
                                 key='-TABLE-',
                                 row_height=25)]]

    specalty_layout = [[sg.Text("Any \"special\" elements will display here!")],
                       [sg.Button("Open Folder")],
                       [sg.Button("Open File")]]

    theme_layout = [[sg.Text("See how elements look under different themes by choosing a different theme here!")],
                    [sg.Listbox(values=sg.theme_list(),
                                size=(20, 12),
                                key='-THEME LISTBOX-',
                                enable_events=True)],
                    [sg.Button("Set Theme")]]

    layout = [[sg.Text('Demo Of (Almost) All Elements', size=(38, 1), justification='center', font=("Helvetica", 16),
                       relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
    layout += [[sg.TabGroup([[sg.Tab('Input Elements', input_layout),
                              sg.Tab('Asthetic Elements', asthetic_layout),
                              sg.Tab('Graphing', graphing_layout),
                              sg.Tab('Specialty', specalty_layout),
                              sg.Tab('Theming', theme_layout),
                              sg.Tab('Output', logging_layout)]], key='-TAB GROUP-')]]

    return sg.Window('All Elements Demo', layout, right_click_menu=right_click_menu_def)


def main():
    window = make_window(sg.theme())

    # This is an Event Loop
    while True:
        event, values = window.read(timeout=100)
        # keep an animation running so show things are happening
        window['-GIF-IMAGE-'].update_animation(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ', values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        elif event == 'About':
            print("[LOG] Clicked About!")
            sg.popup('PySimpleGUI Demo All Elements',
                     'Right click anywhere to see right click menu',
                     'Visit each of the tabs to see available elements',
                     'Output of event and values can be see in Output tab',
                     'The event and values dictionary is printed after every event')
        elif event == 'Popup':
            print("[LOG] Clicked Popup Button!")
            sg.popup("You pressed a button!")
            print("[LOG] Dismissing Popup!")
        elif event == 'Test Progress bar':
            print("[LOG] Clicked Test Progress Bar!")
            progress_bar = window['-PROGRESS BAR-']
            for i in range(1000):
                print("[LOG] Updating progress bar by 1 step (" + str(i) + ")")
                progress_bar.UpdateBar(i + 1)
            print("[LOG] Progress bar complete!")
        elif event == "-GRAPH-":
            graph = window['-GRAPH-']  # type: sg.Graph
            graph.draw_circle(values['-GRAPH-'], fill_color='yellow', radius=20)
            print("[LOG] Circle drawn at: " + str(values['-GRAPH-']))
        elif event == "Open Folder":
            print("[LOG] Clicked Open Folder!")
            folder_or_file = sg.popup_get_folder('Choose your folder')
            sg.popup("You chose: " + str(folder_or_file))
            print("[LOG] User chose folder: " + str(folder_or_file))
        elif event == "Open File":
            print("[LOG] Clicked Open File!")
            folder_or_file = sg.popup_get_file('Choose your file')
            sg.popup("You chose: " + str(folder_or_file))
            print("[LOG] User chose file: " + str(folder_or_file))
        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)

    window.close()
    exit(0)


if __name__ == '__main__':
    main()