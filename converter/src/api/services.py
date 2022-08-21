from api.parser import XMLParser, Context


def get_file_extension(full_file_name: str) -> str:
    file_extension = full_file_name.split('.')[-1]
    return file_extension


def get_strategy_context(file_extension: str) -> Context:
    parser_strategies = {
        "xml": XMLParser(),
    }

    strategy = parser_strategies[file_extension]
    context = Context(strategy)

    return context
