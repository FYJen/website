"""A library contians all validation functions.
"""

def validateDeref(allowedDeref, derefList):
    """Validate the deref list in the query string.
    """
    for deref in derefList:
        if deref not in allowedDeref:
            derefList.remove(deref)

    return derefList