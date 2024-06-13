import os
import flow_operations
import agent_operations
from dotenv import load_dotenv
load_dotenv()

PROJECT_ID = os.getenv('PROJECT_ID')
LOCATION = os.getenv('AGENT_DISPLAY_NAME')
AGENT_DISPLAY_NAME = os.getenv('AGENT_DISPLAY_NAME')
LANGUAGE = os.getenv('LANGUAGE')
TIME_ZONE = os.getenv('TIME_ZONE')

FLOW_DISPLAY_NAME_BOOK = "Reservar Voo"
FLOW_DISPLAY_NAME_CANCEL = "Cancelar Voo"

if __name__ == "__main__":
	# Criar Agente e especificar os parâmetros de projeto, localização, nome do agente, idioma e fuso horário
	agent_response = agent_operations.create_agent(PROJECT_ID, LOCATION, AGENT_DISPLAY_NAME, LANGUAGE, TIME_ZONE)
	print(agent_response)

	# O nome do agente gerado pelo sistema é a chave 'name' na resposta do agente retornada
	agent_name = agent_response.name
	agent_id = agent_name.split("agents/")[1]

	# Listar todos os agentes no projeto e localização especificados
	agent_list = agent_operations.list_agents(PROJECT_ID, LOCATION)
	print(agent_list)

	# Exportar o agente especificado pelo seu nome gerado pelo sistema
	agent_export_response = agent_operations.export_agent(agent_name)
	print(agent_export_response)

	# Criar Fluxo de Reservar Voo e especificar os parâmetros de projeto, localização, nome do agente e idioma
	flow_book_response = flow_operations.create_flow(PROJECT_ID, LOCATION, agent_id, FLOW_DISPLAY_NAME_BOOK, LANGUAGE)
	print(flow_book_response)

	# O nome do fluxo gerado pelo sistema é a chave 'name' na resposta do fluxo retornada
	flow_book_name = flow_book_response.name
	flow_book_id = flow_book_name.split("flows/")[1]

	# Similarmente, criar Fluxo de Cancelar Voo e especificar os parâmetros de projeto, localização, nome do agente e idioma
	flow_cancel_response = flow_operations.create_flow(PROJECT_ID, LOCATION, agent_id, FLOW_DISPLAY_NAME_CANCEL, LANGUAGE)
	print(flow_cancel_response)

	# Similarmente, obter o nome do Fluxo usando a chave 'name' da resposta
	flow_cancel_name = flow_cancel_response.name
	flow_cancel_id = flow_cancel_name.split("flows/")[1]

	# Listar todos os Fluxos no agente especificado no projeto e localização
	flow_list = flow_operations.list_flows(PROJECT_ID, LOCATION, agent_id)
	print(flow_list)

	# Obter o Fluxo usando o ID do Fluxo dentro do agente especificado, projeto e localização
	flow_dsf_response = flow_operations.get_flow(PROJECT_ID, LOCATION, agent_id, FLOW_DSF_ID)
	print(flow_dsf_response)

	# Validar o Fluxo criado usando o nome do fluxo gerado pelo sistema
	flow_book_validate_response = flow_operations.validate_flow(flow_book_name)
	print(flow_book_validate_response)

	# Exportar o fluxo especificado pelo seu nome gerado pelo sistema
	flow_book_export_response = flow_operations.export_flow(flow_book_name)
	print(flow_book_export_response)

	# Deletar o fluxo especificado pelo seu nome gerado pelo sistema
	flow_operations.delete_flow(flow_book_name)
	flow_operations.delete_flow(flow_cancel_name)

	# Deletar o agente especificado pelo seu nome gerado pelo sistema
	agent_operations.delete_agent(agent_name)
