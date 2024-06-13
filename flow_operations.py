from google.cloud.dialogflowcx_v3 import FlowsClient, Flow, CreateFlowRequest, ExportFlowRequest, ValidateFlowRequest

"""
Criar Fluxo no Dialogflow CX com os parâmetros fornecidos:
	- project_id - Projeto Google Cloud onde o Agente existe e onde o Fluxo será criado
	- location - Região onde o Agente reside
	- agent_id - ID do Agente no qual o Fluxo será criado
	- language_code - O idioma de diferentes campos no Fluxo, por exemplo, mensagens de cumprimento. Se não especificado, será usado o idioma do Agente.
A função retorna o Fluxo criado como um objeto do tipo google.cloud.dialogflowcx_v3.types.Flow
Ele contém o nome gerado pelo sistema do fluxo com o formato - projects/<project_id>/locations/<location>/agents/<agent_id>/flows/<ID único criado para o fluxo>
"""
def create_flow(project_id:str, location:str, agent_id:str, flow_display_name:str, language_code:str):

    parent = f"projects/{project_id}/locations/{location}/agents/{agent_id}"

    flows_client = FlowsClient()

    # Inicializa o objeto Flow com os parâmetros obrigatórios como nome do Fluxo e descrição
    flow = Flow(
        display_name=flow_display_name,
        description=f"Este fluxo lida com a conversa para {flow_display_name}" # Você pode parametrizar este método para capturar este valor do usuário.
    )

    # Inicializa o argumento de solicitação com o agente onde ele deve ser criado, o objeto flow criado acima e o código do idioma
    request = CreateFlowRequest(
        parent=parent,
        flow=flow,
        language_code=language_code
    )

    # Faz a solicitação
    response = flows_client.create_flow(request=request)

    return response

"""
Deletar o Fluxo no Dialogflow CX com os parâmetros fornecidos:
	- flow_name - Nome único gerado pelo sistema do Fluxo no formato - projects/<project_id>/locations/<location>/agents/<agent_id>/flows/<ID único criado para o fluxo>
A função não retorna nada
"""
def delete_flow(flow_name:str):
	flows_client = FlowsClient()

	response = flows_client.delete_flow(name=flow_name)
     


"""
Listar todos os Fluxos no Dialogflow CX no Projeto, localização e agente. Os parâmetros necessários são:
	- project_id - Fluxos dentro do Agente deste Projeto Google Cloud serão listados
	- location - Fluxos dentro desta Região serão listados
    - agent_id - Fluxos neste Agente serão listados
A função retorna a lista de Fluxos criados como um objeto do tipo google.cloud.dialogflowcx_v3.services.flows.pagers.ListFlowsPager
"""
def list_flows(project_id:str, location:str, agent_id:str):

	parent = f"projects/{project_id}/locations/{location}/agents/{agent_id}"
	flows_client = FlowsClient()

	response = flows_client.list_flows(parent=parent)

	return response

"""
Treinar o Fluxo no Dialogflow CX no Projeto, localização e agente. Os parâmetros necessários são:
	- project_id - Fluxo dentro do Agente deste Projeto Google Cloud será treinado
	- location - Fluxo dentro desta Região será treinado
    - agent_id - Fluxo neste Agente será treinado
A função retorna a operação de longa duração como um objeto do tipo google.api_core.operation.Operation
O resultado da operação é um objeto do tipo google.protobuf.empty_pb2.Empty
"""
def train_flow(project_id:str, location:str, agent_id:str, flow_id:str):

    flow_name = f"projects/{project_id}/locations/{location}/agents/{agent_id}/flows/{flow_id}"
    flows_client = FlowsClient()

    flow_train_operation = flows_client.train_flow(name=flow_name)

    print("Esta é uma operação longa, Aguardando a conclusão da operação")

    response = flow_train_operation.result()
    return response

"""
Validar o Fluxo no Dialogflow CX no Projeto, localização e agente. Os parâmetros necessários são:
	- flow_name - Nome único gerado pelo sistema do Fluxo no formato - projects/<project_id>/locations/<location>/agents/<agent_id>/flows/<ID único criado para o fluxo>
A função retorna os resultados de validação do fluxo especificado criado como um objeto google.cloud.dialogflowcx_v3.types.FlowValidationResult
"""
def validate_flow(flow_name:str):

    flows_client = FlowsClient()

    request = ValidateFlowRequest(
		name=flow_name
	)

    response = flows_client.validate_flow(request=request)

    return response

"""
Obter o objeto Fluxo no Dialogflow CX usando o ID do Fluxo no Projeto, localização e agente. Os parâmetros necessários são:
	- flow_name - Nome único gerado pelo sistema do Fluxo no formato - projects/<project_id>/locations/<location>/agents/<agent_id>/flows/<ID único criado para o fluxo>
A função retorna o Fluxo especificado pelo ID do Fluxo como um objeto do tipo google.cloud.dialogflowcx_v3.types.Flow
"""
def get_flow(project_id:str, location:str, agent_id:str, flow_id:str):

    flow_name = f"projects/{project_id}/locations/{location}/agents/{agent_id}/flows/{flow_id}"
    flows_client = FlowsClient()

    response = flows_client.get_flow(name=flow_name)

    return response

"""
Exportar o Fluxo no Dialogflow CX com os parâmetros fornecidos:
	- flow_name - Nome único gerado pelo sistema do Fluxo no formato - projects/<project_id>/locations/<location>/agents/<agent_id>/flows/<ID único criado para o fluxo>
A função retorna a operação de longa duração como um objeto do tipo google.api_core.operation.Operation
O resultado da operação é um objeto do tipo google.cloud.dialogflowcx_v3.types.flow.ExportFlowResponse
"""
def export_flow(flow_name:str):

    flows_client = FlowsClient()

    request = ExportFlowRequest(
		name=flow_name
	)

    flow_export_operation = flows_client.export_flow(request=request)

    print("Esta é uma operação longa, Aguardando a conclusão da operação")

    response = flow_export_operation.result()
    return response
