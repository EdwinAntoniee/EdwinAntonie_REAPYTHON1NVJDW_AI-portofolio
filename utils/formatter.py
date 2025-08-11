from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def bubble_chat(message, sender, timestamp):
    if sender == "User":
        align = "right"
        color = "#6398CE"  # Hijau muda untuk user
        float_dir = "right"
        text_align = "right"
        border_radius = "18px 18px 4px 18px"
    else:
        align = "left"
        color = "#3872AC"  # Abu-abu terang untuk AI (lebih gelap dari #f5f6fa)
        float_dir = "left"
        text_align = "left"
        border_radius = "18px 18px 18px 4px"

    html = f"""
    <div style="width:100%; display:flex; justify-content:{align}; margin-bottom:8px;">
        <div style="
            background:{color};
            border-radius:{border_radius};
            padding:10px 16px;
            max-width:70%;
            float:{float_dir};
            text-align:{text_align};
            box-shadow:0 1px 2px rgba(0,0,0,0.04);
            opacity:1;
        ">
            <div style="font-size:15px; color:#000000 !important;">{message}</div>
            <div style="font-size:11px; color:#000000 !important; margin-top:4px;">{timestamp}</div>
        </div>
    </div>
    """
    return html