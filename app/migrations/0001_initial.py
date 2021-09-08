# Generated by Django 3.2.3 on 2021-06-04 06:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('authLevel', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, default='/static/media/icons/person.png', null=True, upload_to='profile-pictures/')),
                ('idUser', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('sss', models.CharField(blank=True, max_length=50, null=True)),
                ('phic', models.CharField(blank=True, max_length=50, null=True)),
                ('hdmf', models.CharField(blank=True, max_length=50, null=True)),
                ('tin', models.CharField(blank=True, max_length=50, null=True)),
                ('dateEmployed', models.DateField(blank=True, null=True)),
                ('dateResigned', models.DateField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('contra', models.BooleanField(blank=True, default=False, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=18, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Child Account',
                'verbose_name_plural': 'Child Accounts',
            },
        ),
        migrations.CreateModel(
            name='AccountGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('normally', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('permanence', models.CharField(max_length=50)),
                ('amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=18, null=True)),
            ],
            options={
                'verbose_name': 'Account Group',
                'verbose_name_plural': 'Account Groups',
            },
        ),
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('datetimeCreated', models.DateTimeField()),
                ('scheduleStart', models.DateTimeField(blank=True, null=True)),
                ('scheduleEnd', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Deliveries',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverID', models.CharField(default='0', max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('status', models.CharField(default='Available', max_length=20)),
            ],
            options={
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Drivers',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('datetimeCreated', models.DateTimeField()),
                ('journalDate', models.DateField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('datetimeApproved', models.DateTimeField(blank=True, null=True)),
                ('approvedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='journalApprovedBy', to=settings.AUTH_USER_MODEL)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='journalCreatedBy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Journal',
                'verbose_name_plural': 'Journals',
            },
        ),
        migrations.CreateModel(
            name='MerchandiseInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('length', models.DecimalField(decimal_places=5, max_digits=20)),
                ('width', models.DecimalField(decimal_places=5, max_digits=20)),
                ('thickness', models.DecimalField(decimal_places=5, max_digits=20)),
                ('purchasingPrice', models.DecimalField(decimal_places=5, max_digits=18)),
                ('sellingPrice', models.DecimalField(decimal_places=5, max_digits=18)),
                ('vol', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('pricePerCubic', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('qtyT', models.IntegerField()),
                ('qtyR', models.IntegerField()),
                ('qtyA', models.IntegerField()),
                ('um', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('turnover', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('totalCost', models.DecimalField(decimal_places=5, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Merchandise Inventory',
                'verbose_name_plural': 'Merchandise Inventories',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('Customer', 'Customer'), ('Vendor', 'Vendor')], max_length=100)),
                ('shippingAddress', models.CharField(blank=True, max_length=512, null=True)),
                ('officeAddress', models.CharField(blank=True, max_length=512, null=True)),
                ('landline', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contactPerson', models.CharField(blank=True, max_length=128, null=True)),
                ('bank', models.CharField(blank=True, max_length=256, null=True)),
                ('bankNo', models.CharField(blank=True, max_length=50, null=True)),
                ('tin', models.CharField(blank=True, max_length=50, null=True)),
                ('crte', models.BooleanField(blank=True, null=True)),
                ('prefferedPayment', models.CharField(blank=True, max_length=50, null=True)),
                ('accountChild', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='party', to='app.accountchild')),
            ],
            options={
                'verbose_name': 'Party',
                'verbose_name_plural': 'Parties',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('password1', models.CharField(blank=True, max_length=255, null=True)),
                ('password2', models.CharField(blank=True, max_length=255, null=True)),
                ('authLevel', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('idUser', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('sss', models.CharField(blank=True, max_length=50, null=True)),
                ('phic', models.CharField(blank=True, max_length=50, null=True)),
                ('hdmf', models.CharField(blank=True, max_length=50, null=True)),
                ('tin', models.CharField(blank=True, max_length=50, null=True)),
                ('dateEmployed', models.DateField(blank=True, null=True)),
                ('dateResigned', models.DateField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registers',
            },
        ),
        migrations.CreateModel(
            name='SalesContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('datetimeCreated', models.DateTimeField()),
                ('dateSold', models.DateField()),
                ('salesOrder', models.IntegerField()),
                ('atcCode', models.CharField(max_length=50)),
                ('amountWithheld', models.DecimalField(decimal_places=5, max_digits=18)),
                ('amountPaid', models.DecimalField(decimal_places=5, max_digits=18, null=True)),
                ('amountDue', models.DecimalField(decimal_places=5, max_digits=18, null=True)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('paymentPeriod', models.CharField(max_length=50)),
                ('chequeNo', models.CharField(max_length=50, null=True)),
                ('dueDate', models.DateField(blank=True, null=True)),
                ('bank', models.CharField(max_length=50)),
                ('remarks', models.TextField(null=True)),
                ('datetimeApproved', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(null=True)),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tempscApprovedBy', to=settings.AUTH_USER_MODEL)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tempscCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tempsalescontract', to='app.journal')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salescontract', to='app.party')),
            ],
            options={
                'verbose_name': 'Sales Contract',
                'verbose_name_plural': 'Sales Contract',
            },
        ),
        migrations.CreateModel(
            name='TempSalesContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('datetimeCreated', models.DateTimeField()),
                ('dateSold', models.DateField()),
                ('subTotal', models.DecimalField(decimal_places=5, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('discountPercent', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('discountPeso', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('taxPeso', models.DecimalField(decimal_places=5, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('totalCost', models.DecimalField(decimal_places=5, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('datetimeApproved', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='scApprovedBy', to=settings.AUTH_USER_MODEL)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='scCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salescontract', to='app.journal')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tempsalescontract', to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name': 'Warehouse',
                'verbose_name_plural': 'Warehouses',
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50, null=True)),
                ('currentDelivery', models.IntegerField(blank=True, null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.driver')),
            ],
            options={
                'verbose_name': 'Truck',
                'verbose_name_plural': 'Trucks',
            },
        ),
        migrations.CreateModel(
            name='TempSCOtherFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.DecimalField(decimal_places=5, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=255)),
                ('salesContract', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tempscotherfees', to='app.tempsalescontract')),
            ],
        ),
        migrations.CreateModel(
            name='TempSCItemsMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('totalCost', models.DecimalField(decimal_places=5, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('merchInventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tempscitemsmerch', to='app.merchandiseinventory')),
                ('salesContract', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tempscitemsmerch', to='app.tempsalescontract')),
            ],
        ),
        migrations.CreateModel(
            name='SCItemsMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('purchasingPrice', models.DecimalField(decimal_places=5, max_digits=8)),
                ('totalPrice', models.DecimalField(decimal_places=5, max_digits=10)),
                ('outputVat', models.DecimalField(decimal_places=5, max_digits=5)),
                ('delivered', models.BooleanField(null=True)),
                ('merchInventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='scitemsmerch', to='app.merchandiseinventory')),
                ('salesContract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='scitemsmerch', to='app.salescontract')),
            ],
            options={
                'verbose_name': 'SC Items Merch',
                'verbose_name_plural': 'SC Items Merchs',
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('datetimeCreated', models.DateTimeField()),
                ('datePurchased', models.DateField()),
                ('atcCode', models.CharField(blank=True, max_length=50, null=True)),
                ('amountWithheld', models.DecimalField(blank=True, decimal_places=5, max_digits=18, null=True)),
                ('amountPaid', models.DecimalField(decimal_places=5, max_digits=18)),
                ('amountDue', models.DecimalField(decimal_places=5, max_digits=18)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('paymentPeriod', models.CharField(max_length=50)),
                ('chequeNo', models.CharField(blank=True, max_length=50, null=True)),
                ('dueDate', models.DateField(blank=True, null=True)),
                ('bank', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('datetimeApproved', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False, null=True)),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='poApprovedBy', to=settings.AUTH_USER_MODEL)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='poCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchaseorder', to='app.journal')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchaseorder', to='app.party')),
            ],
            options={
                'verbose_name': 'Purchase Order',
                'verbose_name_plural': 'Purchase Orders',
            },
        ),
        migrations.CreateModel(
            name='POItemsMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining', models.IntegerField()),
                ('qty', models.PositiveIntegerField()),
                ('purchasingPrice', models.DecimalField(decimal_places=5, max_digits=20)),
                ('totalPrice', models.DecimalField(decimal_places=5, max_digits=20)),
                ('inputVat', models.DecimalField(decimal_places=5, max_digits=20)),
                ('delivered', models.BooleanField(default=False, null=True)),
                ('merchInventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='poitemsmerch', to='app.merchandiseinventory')),
                ('purchaseOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='poitemsmerch', to='app.purchaseorder')),
            ],
            options={
                'verbose_name': 'PO Items Merch',
                'verbose_name_plural': 'PO Items Merchs',
            },
        ),
        migrations.AddField(
            model_name='merchandiseinventory',
            name='warehouse',
            field=models.ManyToManyField(blank=True, related_name='merchandiseinventory', to='app.Warehouse'),
        ),
        migrations.CreateModel(
            name='JournalEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normally', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('amount', models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=18, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=18, null=True)),
                ('accountChild', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='journalentries', to='app.accountchild')),
                ('journal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='journalentries', to='app.journal')),
            ],
            options={
                'verbose_name': 'Journal Entry',
                'verbose_name_plural': 'Journal Entries',
            },
        ),
        migrations.CreateModel(
            name='DeliveryPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='delivery_photos')),
                ('deliveries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deliveryphotos', to='app.deliveries')),
            ],
            options={
                'verbose_name': 'Delivery Photo',
                'verbose_name_plural': 'Delivery Photos',
            },
        ),
        migrations.CreateModel(
            name='DeliveryItemsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryType', models.CharField(max_length=50)),
                ('referenceNo', models.CharField(max_length=50)),
                ('deliveries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deliveryitemsgroup', to='app.deliveries')),
            ],
            options={
                'verbose_name': 'Delivery Item Group',
                'verbose_name_plural': 'Delivery Item Groups',
            },
        ),
        migrations.CreateModel(
            name='DeliveryItemMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('deliveryItemsGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deliveryitemsmerch', to='app.deliveryitemsgroup')),
                ('merchInventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deliveryitemsmerch', to='app.merchandiseinventory')),
            ],
            options={
                'verbose_name': 'Delivery Item Merch',
                'verbose_name_plural': 'Delivery Item Merchs',
            },
        ),
        migrations.CreateModel(
            name='DeliveryDestinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(blank=True, max_length=500, null=True)),
                ('deliveries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deliverydestinations', to='app.deliveries')),
            ],
            options={
                'verbose_name': 'Delivery Destination',
                'verbose_name_plural': 'Delivery Destinations',
            },
        ),
        migrations.AddField(
            model_name='deliveries',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deliveries', to='app.driver'),
        ),
        migrations.AddField(
            model_name='deliveries',
            name='truck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deliveries', to='app.truck'),
        ),
        migrations.CreateModel(
            name='AccountSubGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('accountGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='accountsubgroup', to='app.accountgroup')),
            ],
            options={
                'verbose_name': 'Account Sub-Group',
                'verbose_name_plural': 'Account Sub-Groups',
            },
        ),
        migrations.AddField(
            model_name='accountchild',
            name='accountSubGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='accountchild', to='app.accountsubgroup'),
        ),
        migrations.AddField(
            model_name='accountchild',
            name='me',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='accountchild', to='app.accountchild'),
        ),
    ]