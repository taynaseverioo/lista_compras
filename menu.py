import tkinter as tk
from tkinter import messagebox

# Funções simuladas de backend
def simular_login(usuario, senha):
    if usuario == 'admin' and senha == 'admin123':
        return {'message': 'Login realizado com sucesso'}
    else:
        return {'error': 'Nome de usuário ou senha incorretos'}

lista_compras = []

def simular_adicionar_item(item):
    lista_compras.append(item)
    return {'mensagem': 'Item adicionado com sucesso!', 'lista_compras': lista_compras}

def simular_remover_item(item):
    if item in lista_compras:
        lista_compras.remove(item)
        return {'mensagem': 'Item removido com sucesso!', 'lista_compras': lista_compras}
    else:
        return {'erro': 'Item não encontrado na lista.'}

# Classe base para os handlers
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)

# Handler para login
class LoginHandler(Handler):
    def handle(self, request):
        if request['action'] == 'login':
            response = simular_login(request['username'], request['password'])
            if 'error' in response:
                messagebox.showerror("Erro de Login", response['error'])
            else:
                messagebox.showinfo("Login", response['message'])
        else:
            return super().handle(request)

# Handler para adicionar item
class AddItemHandler(Handler):
    def handle(self, request):
        if request['action'] == 'add_item':
            response = simular_adicionar_item(request['item'])
            if 'erro' in response:
                messagebox.showerror("Erro ao Adicionar Item", response['erro'])
            else:
                messagebox.showinfo("Item Adicionado", response['mensagem'])
                shopping_list_box.insert(tk.END, request['item'])
        else:
            return super().handle(request)

# Handler para remover item
class RemoveItemHandler(Handler):
    def handle(self, request):
        if request['action'] == 'remove_item':
            response = simular_remover_item(request['item'])
            if 'erro' in response:
                messagebox.showerror("Erro ao Remover Item", response['erro'])
            else:
                messagebox.showinfo("Item Removido", response['mensagem'])
                shopping_list_box.delete(request['index'])
        else:
            return super().handle(request)

# Configurar a cadeia de handlers
handler_chain = LoginHandler(AddItemHandler(RemoveItemHandler()))

# Função para adicionar um produto à lista de compras
def add_to_shopping_list(produto):
    request = {'action': 'add_item', 'item': produto}
    handler_chain.handle(request)

# Função para lidar com o login
def handle_login():
    username = entry_username.get()
    password = entry_password.get()
    request = {'action': 'login', 'username': username, 'password': password}
    handler_chain.handle(request)

# Função para remover um produto da lista de compras
def remove_from_shopping_list():
    selected_index = shopping_list_box.curselection()
    if selected_index:
        selected_item = shopping_list_box.get(selected_index)
        request = {'action': 'remove_item', 'item': selected_item, 'index': selected_index}
        handler_chain.handle(request)

# Configuração da tela principal do sistema
root_main = tk.Tk()
root_main.title("Sistema de Compras")
root_main.geometry("800x600")

# Título da tela principal
label_title_main = tk.Label(root_main, text="Bem-vindo ao Sistema de Compras", font=("Helvetica", 20))
label_title_main.pack(pady=20)

# Entradas de usuário para login
label_username = tk.Label(root_main, text="Usuário:")
label_username.pack()
entry_username = tk.Entry(root_main)
entry_username.pack()

label_password = tk.Label(root_main, text="Senha:")
label_password.pack()
entry_password = tk.Entry(root_main, show="*")
entry_password.pack()

# Botão para login
button_login = tk.Button(root_main, text="Login", command=handle_login)
button_login.pack(pady=10)

# Lista de compras
label_shopping_list = tk.Label(root_main, text="Lista de Compras", font=("Helvetica", 16))
label_shopping_list.pack()

shopping_list_box = tk.Listbox(root_main, width=50, height=10)
shopping_list_box.pack()

# Botão para remover item da lista
button_remove_item = tk.Button(root_main, text="Remover Item", command=remove_from_shopping_list)
button_remove_item.pack(pady=10)

# Botão para sair do sistema
button_exit_main = tk.Button(root_main, text="Sair", font=("Helvetica", 12), command=root_main.quit)
button_exit_main.pack(pady=20)

# Iniciar a aplicação
root_main.mainloop()

