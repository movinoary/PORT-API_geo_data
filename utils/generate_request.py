def generate_request(request):
    data= {
    'create_by': request.args.get('create_by'),
    'x_signature': request.headers.get('x-signature')
    }
    return data