from django.shortcuts import render
from django.http import HttpResponse

CSS_PADRAO = """
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; background-color: #f4f4f9; color: #333; max-width: 800px; margin: 40px auto; padding: 20px; }
    h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
    a { display: inline-block; margin-top: 10px; padding: 10px 15px; background-color: #3498db; color: white; text-decoration: none; border-radius: 5px; transition: 0.3s; }
    a:hover { background-color: #2980b9; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }
    th, td { padding: 12px; border: 1px solid #ddd; text-align: left; }
    th { background-color: #3498db; color: white; }
    tr:nth-child(even) { background-color: #f2f2f2; }
    ul { list-style-type: none; padding: 0; }
    li { background: white; margin: 5px 0; padding: 10px; border-left: 5px solid #3498db; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
</style>
"""

def pagina_inicial(request):
    return HttpResponse(f'''
<!DOCTYPE html>
<html>
  <head>
    <title>Sistema</title>
    {CSS_PADRAO}
  </head>
  <body>
    <h1>sistemaslegais</h1>
    <p>projetos aleatorios</p>
    <nav>
        <a href="http://127.0.0.1:8000/pagina2/">página sobre</a><br>
        <a href="http://127.0.0.1:8000/pagina3/">página projetos</a><br>
        <a href="http://127.0.0.1:8000/pagina4/">página contato</a>
    </nav>
  </body>
</html>
''')

def pagina_sobre(request):
    return HttpResponse(f'''
<!DOCTYPE html>
<html>
  <head>
    <title>Sistemas</title>
    {CSS_PADRAO}
  </head>
  <body>
    <h1>explicação do sistema</h1>
    <p>nenhuma</p>
    <p><strong>Equipe:</strong> Nome da equipe</p>
    <a href="http://127.0.0.1:8000/pagina1/"> VOLTAR </a>
  </body>
</html>
''')

def pagina_projetos(request):
    return HttpResponse(f'''
<!DOCTYPE html>
<html>
  <head>
    <title>Sistemas</title>
    {CSS_PADRAO}
  </head>
  <body>
    <h1>listas de projetos</h1>
    <table>
      <thead>
        <tr>
          <th>Projeto</th>
          <th>Descrição</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Projeto 1</td>
          <td>Descrição detalhada do projeto 1</td>
        </tr>
        <tr>
          <td>Projeto 2</td>
          <td>Descrição detalhada do projeto 2</td>
        </tr>
      </tbody>
    </table>
    <br>
    <a href="http://127.0.0.1:8000/pagina1/"> VOLTAR </a>
  </body>
</html>
''')

def pagina_contato(request):
    return HttpResponse(f'''
<!DOCTYPE html>
<html>
  <head>
    <title>Sistemas</title>
    {CSS_PADRAO}
  </head>
  <body>
    <h1>contatos</h1>
    <ul>
      <li><strong>Email:</strong> mily@gmail.com</li>
      <li><strong>Telefone:</strong> 81 9 8765-6374</li>
      <li><strong>Agência:</strong> Pyhro Agência</li>
      <li><strong>Membros:</strong> Emily & Jemerson</li>
    </ul>
    <a href="http://127.0.0.1:8000/pagina1/"> VOLTAR </a>
  </body>
</html>
''')