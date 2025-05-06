from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField()
    email = models.CharField(unique=True)
    senha = models.CharField()
    tipo_usuario = models.CharField()
    ativo = models.BooleanField(blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.CharField()
    crm = models.CharField(unique=True)
    especialidade = models.CharField()
    telefone = models.CharField(blank=True, null=True)
    email = models.CharField(unique=True)
    data_contratacao = models.DateField()
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField()
    data_nascimento = models.DateField()
    cpf = models.CharField(unique=True)
    endereco = models.CharField(blank=True, null=True)
    telefone = models.CharField(blank=True, null=True)
    email = models.CharField(unique=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='id_medico')
    data_consulta = models.DateTimeField()
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    id_prontuario = None #models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'


class Prontuario(models.Model):
    id_prontuario = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_paciente')
    id_medico = models.ForeignKey(Medico, models.DO_NOTHING, db_column='id_medico')
    id_consulta = models.OneToOneField(Consulta, models.DO_NOTHING, db_column='id_consulta')
    data_registro = models.DateTimeField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    prescricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prontuario'


