from django.db import models

class CommandJob(models.Model):
    COMMAND_TYPES = [
        ('REBOOT', 'System Reboot'),
        ('UPDATE', 'Package Update (pip/choco)'),
        ('RENAME', 'Hostname Normalization'),
        ('CUSTOM', 'Custom Shell Script')
    ]
    target_node = models.CharField(max_length=100, default='ALL-LAB-PCS')
    command_type = models.CharField(max_length=20, choices=COMMAND_TYPES)
    raw_payload = models.TextField()
    status = models.CharField(max_length=20, choices=[('QUEUED','Queued'), ('EXECUTED','Executed'), ('FAILED','Failed')], default='QUEUED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.target_node} - {self.command_type} ({self.status})"
