from rest_framework import serializers
from .models import Team, Member


class MemberSerializerForTeam(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'username')


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all(), many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'members')


class MemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Member
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'email', 'team')
        read_only_fields = ['id', ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance