def get_selected_key(pointed_key, index_thumb_distance, dist_threshold=20):
    if pointed_key and index_thumb_distance <= dist_threshold:

        return pointed_key

    return None