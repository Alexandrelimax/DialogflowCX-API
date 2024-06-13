""""
AgentsClient e ExportAgentRequest são classes necessárias da biblioteca 
google.cloud.dialogflowcx_v3 para interagir com agentes no Dialogflow CX.
Agent é um tipo de mensagem específico que representa um agente no Dialogflow CX.
"""
from google.cloud.dialogflowcx_v3 import AgentsClient,ExportAgentRequest
from google.cloud.dialogflowcx_v3.types.agent import Agent

"""
Objetivo: Criar um novo agente no Dialogflow CX.
Parâmetros:
project_id: ID do projeto do Google Cloud onde o agente será criado.
location: Região onde o agente residirá.
agent_name: Nome de exibição do agente.
language_code: Código de idioma padrão do agente.
time_zone: Fuso horário seguido pelo agente.
Retorno: A resposta da criação do agente, que contém informações sobre o agente criado.
"""
def create_agent(project_id:str, location:str, agent_name:str, 
                language_code:str, time_zone:str):

    parent = f"projects/{project_id}/locations/{location}"
    agents_client = AgentsClient()

    agent = Agent(
        display_name=agent_name,
        default_language_code=language_code,
        time_zone=time_zone
    )

    response = agents_client.create_agent(request={"agent": agent, "parent": parent})
    return response


"""
Objetivo: Deletar um agente existente no Dialogflow CX.
Parâmetros:
agent_name: Nome único do agente no formato projects/<project_id>/locations/<location>/agents/<Unique ID>.
Retorno: Nenhum retorno explícito, apenas realiza a operação de deleção.
"""
def delete_agent(agent_name:str):
    agents_client = AgentsClient()
    response = agents_client.delete_agent(name=agent_name)
    print(response)


"""
Objetivo: Listar todos os agentes criados em um projeto e região específicos.
Parâmetros:
project_id: ID do projeto do Google Cloud onde os agentes serão listados.
location: Região dos agentes que serão listados.
Retorno: A resposta da listagem dos agentes, que é um objeto
 google.cloud.dialogflowcx_v3.services.agents.pagers.ListAgentsPager.
"""
def list_agents(project_id:str, location:str):

    parent = f"projects/{project_id}/locations/{location}"
    agents_client = AgentsClient()

    response = agents_client.list_agents(parent=parent)
    return response


"""
Objetivo: Listar todos os agentes criados em um projeto e região específicos.
Parâmetros:
project_id: ID do projeto do Google Cloud onde os agentes serão listados.
location: Região dos agentes que serão listados.
Retorno: A resposta da listagem dos agentes, que é um objeto 
google.cloud.dialogflowcx_v3.services.agents.pagers.ListAgentsPager.
"""
def export_agent(agent_name:str):

    agents_client = AgentsClient()
    request = ExportAgentRequest(
        name=agent_name
    )

    export_operation = agents_client.export_agent(request=request)
    print("Waiting for the Operation to complete")

    response = export_operation.result()
    return response