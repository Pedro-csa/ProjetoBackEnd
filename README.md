Sobre o Projeto

O projeto do VidaPlus é um sistema web de gestão hospitalar desenvolvido com o objetivo de oferecer uma solução prática e eficiente para o controle de pacientes, médicos e consultas. 
Construído utilizando a linguagem Python, juntamente com o framework Django e o banco de dados relacional PostgreSQL, o sistema permite a centralização das informações em uma interface administrativa de maneira clara e obejtiva.

Durante o desenvolvimento, foram aplicadas boas práticas do desenvolvimento, como modelagem de dados com ORM, separação de responsabilidades entre camadas e autenticação de usuários. 
A aplicação permite o gerenciamento completo via formulários HTML tradicionais ou requisições externas em formato JSON, facilitando a integração com outras interfaces e ferramentas como o Postman que foi o utilizado para testes.

O foco principal do desenvolvimento é centrado em quatro classes fundamentais para a lógica do sistema: Usuario, Medico, Paciente e Consulta.
Sendo o Usuario o administrador do sistema, o qual controla o CRUD de Médico, Paciente e Consulta.

**Para a execução do projeto:**
Deve ser criado um admin (super user), para isso basta utilizar o seguinte comando no CMD:

LOCAL > **python manage.py createsuperuser**

Exemplo: **C:\Users\SGHSS> python manage.py createsuperuser**

Basta inserir um login e senha e confirmar. 

Para iniciar o servidor local, utilize o terminal com os seguintes comandos:

LOCAL > **python manage.py runserver**

Exemplo: **C:\Users\SGHSS> python manage.py runserver**

![Tela Inicial](https://github.com/user-attachments/assets/eeb3d841-89e8-458a-b1eb-57004d1cb42b)

![Tela de Login](https://github.com/user-attachments/assets/939f724f-bf30-4c04-b529-1c51c480e699)

![Tela Administrativa](https://github.com/user-attachments/assets/e4abe330-e98c-4444-98eb-d91649e0bdc2)
