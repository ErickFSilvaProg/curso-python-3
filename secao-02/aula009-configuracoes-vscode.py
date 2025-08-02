"""
No PowerShell, verifique o "ExecutionPolicy": Get-ExecutionPolicy
Se estiver "Restricted", altere-o para "RemoteSigned": Set-ExecutionPolicy AllSigne -Force
                                                  (ou) Set-ExecutionPolicy RemoteSigned -Force

- Políticas de Execução:

    Restricted:
        A política mais restritiva. Impede a execução de qualquer script e é a configuração padrão em muitos sistemas.

    AllSigned:
        Permite a execução de scripts, mas apenas aqueles que foram assinados digitalmente por um editor confiável.

    RemoteSigned:
        Permite a execução de scripts locais sem assinatura e scripts baixados da internet que foram assinados digitalmente.

    Unrestricted:
        A política mais permissiva. Permite a execução de todos os scripts, incluindo aqueles não assinados. É recomendável usar essa política apenas em ambientes confiáveis ou para fins de teste.

    Bypass:
        Ignora todas as restrições e executa todos os scripts. É semelhante ao Unrestricted, mas com menos avisos.

    Default:
        Redefine a política de execução para a política padrão do sistema.

Para criar o "Ambiente Virtual Python: venv", execute: python -m venv venv
Para ativar o "Ambiente Virtual Python: venv", execute: .\venv\Scripts\activate
"""

print("Configurações no Python")