from rest_framework import permissions

class IsAuthorUpdateOrReadonly(permissions.BasePermission):
    # 인증된 유저에 한해 목록 조회/포스팅 등록 허용
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # superuser에게는 삭제 권한을 부여하고 작성자에게만 수정 권한 부여
    def has_object_permission(self, request, view, obj):
        # 조회 요청(GET, HEAD, OPTIONS)에 대해서는 인증 여부에 상관없이 허용
        if request.method is permissions.SAFE_METHODS:
            return True
        # 삭제 요청의 경우  superuser에 한해 허용
        if request.method == 'DELETE':
            return request.user.is_superuser

        # PUT 요청에 대해 작성자일 경우에만 허용
        return obj.author == request.user
