from adapters import agents
import dotenv
import os
import re

dotenv.load_dotenv()
hash = os.getenv("HASH")
_thisdir = os.path.dirname(os.path.abspath(__file__))
dirout = f"{_thisdir}/../{hash}/yamlout"

examfiles = [
    "20200812 - EEG - Laudo.pdf",
    "20201019 - Sangue 1 - OswaldoCruz.pdf",
    "20201019 - Sangue 2 - OswaldoCruz.pdf",
    "20201031 - Urina evolutivo.pdf",
    "20201031 - Urina.pdf",
    "20210109 - Great Plains - Igg 1.pdf",
    "20210109 - Great Plains - Igg 2.pdf",
    "20210109 - Sangue 1 - Dra Simone.pdf",
    "20210111 - ExameDraSimone - Analise Cromossomica Microarray.pdf",
    "20210111 - Sangue 2 - Dra Simone.pdf",
    "20210126 - Great Plains - Ácidos Orgânicos.pdf",
    "20210220 - Dra. Simone - Ige.pdf",
    "20210220 - Dra. Simone - Selenio.pdf",
    "20210804_Giardia.pdf",
    "20210805_Leveduras_ALTERADO.pdf",
    "20210810_Toxina A e B.pdf",
    "20210811_Calprotectina.pdf",
    "20210813_Urina_ALTERADO.pdf",
    "20210816_Parasitologico_ALTERADO.pdf",
    "20210818_Oligossacaridios.pdf",
    "20210921_Exames de Sangue Setembro.pdf",
    "20210922 - Serotonina e FNTA.pdf",
    "20211025 - ATEC.pdf",
    "20220109_(MCSEM.2501)_Elementos Toxicos e Essenciais - Cabelo.pdf",
    "20220110_GreatPlains_(MOATSEM.2501)_Microbial Organical Acids Test.pdf",
    "20220201 - ATEC.pdf",
    "20220926_Resultado_exame_coprologico_LabLemos.pdf",
    "20220929_Resultados_exames_sangue_smartlabs_1.pdf",
    "20220929_Resultados_exames_sangue_smartlabs_2.pdf",
    "20221122 - Raio-X punho.pdf",
    "20230131 - DraCristiane - OswaldoCruz - exame sangue - selenio.pdf",
    "20230131 - DraCristiane - OswaldoCruz - exame sangue.pdf",
    "20230318 - GreatPlains OAT eng.pdf",
    "20230322 - GreatPlains CSAP eng.pdf",
    "20230418 - Exoma.pdf",
    "20230705 - Mitoswab.pdf",
    "20230710 - Frat test - Ilyad Neurosciences.pdf",
    "20230820 - GPL - CSAP.pdf",
    "20230914 - Oswaldo Cruz - Exame Sangue - TNF alfa.pdf",
    "20230914 - Oswaldo Cruz - Exames Sangue.pdf",
    "20231020_EEG_Laudo.pdf",
    "20231020_EEG_Laudo_VEEG.pdf",
    "20231020_EEG_Tracado1de4.pdf",
    "20231020_EEG_Tracado2de4.pdf",
    "20231020_EEG_Tracado3de4.pdf",
    "20231020_EEG_Tracado4de4.pdf",
    # "20231217 - GPL - CSAP.pdf",
    "20240123 - Bioraras - Relatorio_exoma.pdf",
    "20240413 - LaboratorioLemos-Copromax.pdf",
]

def main():
    for ef in examfiles[5:]:
        try:
            ask_and_save("summarizer", "summarize_exam", f"{_thisdir}/../{hash}/drive/Exams/{ef}", dirout)
            print(f"Processed {ef}")
        except Exception as e:
            print(f"Error processing {ef}: {e}")

def ask_and_save(agent, prompt, filein, dirout):
    agent_instructions = load_instructions(agent)
    agent_id = agents.get_or_create(agent, agent_instructions)
    response = agents.get_yaml_response(agent_id, load_prompt(prompt), filein)
    save_yaml_response(filein, dirout, prompt, response)
    # pass

def load_instructions(agent):
    with open(f"{_thisdir}/agents/{agent}.txt", "r") as file:
        return file.read()

def load_prompt(prompt):
    with open(f"{_thisdir}/prompts/{prompt}.txt", "r") as file:
        return file.read()

def save_yaml_response(filein, dirout, prompt, response):
    yaml_response = extract_code_blocks(response)[0]
    filename = filein.split('/')[-1]
    with open(f"{dirout}/{prompt}-{filename}.yaml", "w") as file:
        file.write(yaml_response)
    pass

def extract_code_blocks(markdown_text):
    code_block_pattern = re.compile(r'```(?:\w+)?\n(.*?)\n```', re.DOTALL)
    code_blocks = [block.strip() for block in code_block_pattern.findall(markdown_text)]
    return code_blocks

if __name__ == "__main__":
    main()