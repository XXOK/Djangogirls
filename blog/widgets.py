from django import forms

class LocationWidget(forms.TextInput):
    template_name = 'widgets/location_widget.html' # 위젯의 탬플릿 지정

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs) # 기존 어트리뷰트 가져오기
        attrs['readonly'] = True # 읽기 전용 속성 추가
        # attrs['placeholder'] = '지도 위치를 지정해주세요'
        # attrs['style'] = 'background-color: #eee; border: 0;'
        attrs['hidden'] = True # 히든 필드 속성 추가

        return attrs