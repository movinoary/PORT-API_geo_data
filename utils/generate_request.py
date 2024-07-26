def generate_request(request):
    data= {
    'create_by': request.args.get('createBy'),
    'x_signature': request.headers.get('x-signature')
    }
    return data