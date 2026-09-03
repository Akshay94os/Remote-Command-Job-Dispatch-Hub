from django.shortcuts import render, redirect, get_object_or_404
from .models import CommandJob

def index(request):
    if request.method == 'POST':
        target = request.POST.get('target_node', 'ALL-NODES')
        cmd_type = request.POST.get('command_type')
        payload = request.POST.get('raw_payload')
        CommandJob.objects.create(target_node=target, command_type=cmd_type, raw_payload=payload)
        return redirect('job_home')

    jobs = CommandJob.objects.order_by('-created_at')[:20]
    return render(request, 'jobs/index.html', {'jobs': jobs})

def execute_job(request, pk):
    job = get_object_or_404(CommandJob, id=pk)
    job.status = 'EXECUTED'
    job.save()
    return redirect('job_home')
