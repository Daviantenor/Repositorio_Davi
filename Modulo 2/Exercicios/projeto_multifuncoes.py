import os
import flet as ft
vazio=""
pasta=""
def main(page:ft.Page):
    page.title=("Entrada de usuário")
    page.theme_mode="Dark"
    def criar_pasta(e):
        global pasta
        pasta = texto_entrada.value
        try:
            os.mkdir(pasta)
            informativo.value=f"pasta criada com sucesso"
        
        except FileExistsError:
            informativo.value=f"a pasta'{pasta}'foi criada"
        
        page.update()
    
    def criar_arquivo(e):
        global pasta
        try:   
            arquivo=texto_entrada2.value
            if pasta== "":
                open(f"{arquivo}", "w").close()
                informativo.value = f"Arquivo criado: '{arquivo}.txt'"
            else:
                open(f"{pasta}/{arquivo}", "w").close()
                informativo.value = f"Arquivo criado: '{pasta}/{arquivo}.txt'"
        except Exception as erro:
            informativo.value=f"Erro ao criar pasta{erro}"
            informativo.color="red"
    
        page.update()
        
    def remover_pasta(e):
        pasta=texto_entrada.value
        try:
            os.rmdir(pasta)
            informativo.value=f"pasta apagada com sucesso"
        except FileExistsError:
            informativo.value=f"deu algum erro'{pasta}'"
        
        page.update()
    def remover_arquivo(e):

        arquivo = texto_entrada2.value
        if pasta=="":

            os.remove(f"{arquivo}")
            informativo.value=f"arquivo  externo apagado com sucesso:'{arquivo}'"
           
        else:
                os.remove(f"{pasta}/{arquivo}")
                informativo.value=f"arquivo apagado com sucesso{pasta}/{arquivo}"
            
        page.update()
    
    texto_entrada=ft.TextField(label="Crie ou remova uma pasta.")
    texto_entrada2=ft.TextField(label="Crie ou remova um arquivo")
    botao_criar_pasta=ft.ElevatedButton("criar pasta",on_click=criar_pasta,bgcolor="Green",color="white",width=300)
    botao_remover_arquivo=ft.ElevatedButton("remover arquivo",on_click=remover_arquivo,bgcolor="red",color="white",width=300)
    botao_remover_pasta=ft.ElevatedButton("remover pasta",on_click=remover_pasta,bgcolor="yellow",color="white",width=300)
    botao_criar_arquivo=ft.ElevatedButton("criar arquivo",on_click=criar_arquivo,bgcolor="orange",color="white",width=300)
   
    informativo=ft.Text("",size=25,color="Green")
    page.add(ft.Row([texto_entrada]),
             ft.Row([texto_entrada2]),
            ft.Row([botao_criar_pasta]),
            ft.Row([botao_remover_arquivo]),
            ft.Row([botao_remover_pasta]),
            ft.Row([botao_criar_arquivo]),
            ft.Row([informativo]))
ft.app(target=main)
