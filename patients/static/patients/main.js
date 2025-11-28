document.addEventListener("DOMContentLoaded", function () {
    const toast = document.querySelectorAll('.toast')

    toast.forEach(toast => {
        setTimeout(() => {
            toast.style.transition = "opacity 0.5s";
            toast.style.opacity = "0";
            setTimeout(() =>{
                toast.remove(), 500
            });
        }, 3000);
        toast.addEventListener("click", () => toast.remove());
    });
});