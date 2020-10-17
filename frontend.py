# frontend.py
import PySimpleGUI as sg      

layout = [[sg.Text('Input the job link you would like to autofill')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('JobChamp', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    

sg.popup('You entered', text_input)