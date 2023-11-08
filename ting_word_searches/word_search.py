def exists_word(word, instance):
    word = word.lower()
    return_obj = []
    for index in range(len(instance)):
        data_search = {}
        for i in range(instance.search(index)["qtd_linhas"]):
            if word in instance.search(index)["linhas_do_arquivo"][i].lower():
                if len(data_search) == 0:
                    data_search["palavra"] = word
                    data_search["arquivo"] = instance.search(index)["nome_do_arquivo"]
                    data_search["ocorrencias"] = [{
                        "linha": i + 1,
                    }]
                    return_obj.append(data_search)
                else:
                    data_search["ocorrencias"].append({
                        "linha": i + 1,
                    })
    return return_obj


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
