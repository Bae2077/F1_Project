from django.contrib.auth.decorators import login_required, permission_required


def permiso_requerido(permiso):
    def decorador(vista):
        return login_required(
            permission_required(
                permiso,
                raise_exception=True
            )(vista)
        )

    return decorador