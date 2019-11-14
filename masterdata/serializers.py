from masterdata.models import *
from rest_framework import serializers




class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportDetails
        # fields =   '__all__'
        fields = ['result_status', 'std', 'Social', 'Math', 'Year', 'Total', 'Sci', 'created_on', 'Grade', 'active', 'Language', 'modified_on', 'report_details_id', 'student','student_name']

    student_name = serializers.SerializerMethodField('get_student_name')
    def get_student_name(self, obj):
        return obj.student.student_name
