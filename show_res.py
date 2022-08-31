import PySimpleGUI as sg
sg.theme('DarkAmber') 


layout = [[
    sg.Frame('',[[
        sg.Text(0, font=("Arial", 250), key="score1", justification="center", pad=(0, 0)),      
    ]], size=(500, 500), element_justification="center", expand_x= True, expand_y= True, vertical_alignment='center', pad=(0, 0)),    
    sg.Frame('',[[
    sg.Text(0, font=("Arial", 250), key="score2", justification="center", pad=(0, 0)),      
    ]], size=(500, 500), element_justification="center", expand_x= True, expand_y= True, vertical_alignment='center', pad=(0, 0))
]]




window = sg.Window('App', layout, size=(1000, 500), resizable=True)


while True:
    
    with open("results.txt", "r") as f:
        lines = f.readlines()
        score1 = lines[0].split(",")[0]
        score2 = lines[0].split(",")[1]
        
    event, values = window.Read(timeout=10)
  
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    
    window["score1"].update(score1)
    window["score2"].update(score2)

    
window.close()    

