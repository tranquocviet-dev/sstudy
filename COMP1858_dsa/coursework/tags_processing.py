import ast
def parse_tags(tag_str):
    try:
        return ast.literal_eval(tag_str)
    except Exception:
        return []

def combine_tags(tag_lists):
    all_tags = set()
    for tag_list in tag_lists:
        for tag in tag_list:
            all_tags.add(tag.strip())
    return list(all_tags)
