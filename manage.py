import os
import sys

def main():

    # Definição da configuração padrão do Django pelo arquivo settings.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vidaplus.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError() from exc
    execute_from_command_line(sys.argv)
    
# Executa a função principal
if __name__ == '__main__':
    main()
