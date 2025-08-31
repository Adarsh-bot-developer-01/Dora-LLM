
def check_force_join(user_id, channel_id, group_id, bot):
    try:
        # Channel check
        member = bot.get_chat_member(channel_id, user_id)
        if member.status in ["left", "kicked"]:
            return False

        # Group check
        member = bot.get_chat_member(group_id, user_id)
        if member.status in ["left", "kicked"]:
            return False

        return True
    except Exception:
        return False

def log_update(msg):
    with open("logs/updates.log", "a") as f:
        f.write(msg + "\n")
