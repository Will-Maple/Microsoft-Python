def make_sandwich(bread_type: str, filling: str, cheese: str = "none", toasted: bool = False):
    """
    Creates a sandwhich with the following...
    
    Args:
        bread_type (str)
        filling (str)
        cheese (str, optional) defaults to 'none'
        toasted (boolean, optional) defaults to False
    """
    if toasted:
        sentence_start = "Making a toasted"
    else:
        sentence_start = "Making a"
    if cheese != 'none':
        sentence_end = f" and {cheese} cheese."
    else:
        sentence_end = "."

    return f"{sentence_start} {bread_type} sandwich with {filling}{sentence_end}"