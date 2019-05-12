def is_issue(args):
    try:
        return args.type in ['i', 'issue'] and args.id
    except:
        return False


def has_status_flag(args):
    try:
        return args.status
    except:
        return False
