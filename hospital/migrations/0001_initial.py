from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('senha', models.CharField(max_length=128)),
                ('tipo_usuario', models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Médico', 'Médico'), ('Recepcionista', 'Recepcionista')])),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('endereco', models.CharField(max_length=255, null=True, blank=True)),
                ('telefone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('crm', models.CharField(max_length=20, unique=True)),
                ('especialidade', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('data_contratacao', models.DateField()),
                ('usuario', models.OneToOneField(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('diagnostico', models.TextField(null=True, blank=True)),
                ('prescricao', models.TextField(null=True, blank=True)),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_consulta', models.DateTimeField()),
                ('descricao', models.TextField(null=True, blank=True)),
                ('status', models.CharField(default='Agendada', max_length=20, choices=[('Agendada', 'Agendada'), ('Realizada', 'Realizada'), ('Cancelada', 'Cancelada')])),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Paciente')),
                ('prontuario', models.OneToOneField(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Prontuario')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, null=True)),
                ('contato', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('assunto', models.CharField(max_length=100, null=True)),
                ('mensagem', models.TextField(null=True)),
                ('data_mensagem', models.DateField(null=True)),
                ('lido', models.BooleanField(default=False)),
            ],
        ),
    ]
