import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

#keyVaultName = os.environ["KEY_VAULT_NAME"]
keyVaultName = 'barry-azure-keyvault'
KVUri = "https://" + keyVaultName + ".vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

def getKey(keyName):
    client.get_secret(keyName)