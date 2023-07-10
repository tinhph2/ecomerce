class Cart():
    def __init__(self, request):
        self.session = request.session
        # Nếu user đã có session thì lấy session hiện tại
        cart = self.session.get('session_key')
        # Tạo session mới nếu user chưa có
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart
