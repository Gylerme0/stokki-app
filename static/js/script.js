document.addEventListener('DOMContentLoaded', () => {
    console.log('Stokki Dashboard Loaded');
    
    // Future interactions can be added here
    const actionBtns = document.querySelectorAll('.action-btn');
    actionBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            console.log('Action clicked:', btn.textContent.trim());
        });
    });
});
