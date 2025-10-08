import flet as ft

def main(page:ft.Page):

        page.title="IMC(Índice de massa corporal)"
        page.theme_mode="dark"
        def imc_o(e):
            try:   
                imc =float(te_peso.value)  /(float(te_alt.value) * float(te_alt.value))
                page.open(ft.SnackBar(ft.Text(f'seu imc é:{imc}')))
            
        
            except:
                informativo.value="erro"
 
    

        te_peso=ft.TextField(label="Digite seu peso")
        te_alt=ft.TextField(label="Digite sua altura")
        
        informativo=ft.Text("",size=25,color="Green")
        botao_imc_o=ft.ElevatedButton("calcular imc",on_click=imc_o,bgcolor="orange",color="white",width=300)
        ft.Text("",size=25,color="Green")
        page.add(ft.Row([te_peso])),
        page.add(ft.Row([te_alt])),
        page.add(ft.Row([botao_imc_o]))
ft.app(target=main)
