window.addEventListener('load', function(){
    const canvas01 = document.getElementById('canvas_01');
    const ctx01 = canvas01.getContext('2d');
    canvas01.width = window.innerWidth;
    canvas01.height = window.innerHeight;

    ctx01.lineWidth = 10;
    ctx01.lineCap = 'round';
    ctx01.strokeStyle = 'hsl(60, 100%, 50%)';
    ctx01.shadowColor = 'rgba(0, 0, 0, 2';
    ctx01.shadowOffsetY = 10;
    ctx01.shadowOffsetX = 5;
    ctx01.shadowBlur = 5;

    // effect
    let size = canvas01.width < canvas01.height ? canvas01.width * 0.3 : canvas01.height * 0.3;
    let sides = 5;
    let branches = 4;
    let maxLevel = 3;
    let spread = 0.35;
    let scale = 0.55;
    ctx01.save();
    ctx01.translate(canvas01.width/2, canvas01.height/2);
    ctx01.rotate(-1.55);
    ctx01.scale(scale, scale);
    
    function drawBranch(level){
        if (level > maxLevel) return;
        ctx01.beginPath();
        ctx01.moveTo(0, 0);
        ctx01.lineTo(size, 0);
        ctx01.stroke();

        for (let i = 0; i < branches; i++){
            ctx01.save();
            ctx01.translate(size - (size/branches) * i, 0);
            ctx01.rotate(spread);
            ctx01.scale(scale, scale);
            drawBranch(level + 1);
            ctx01.restore();

            ctx01.save();
            ctx01.translate(size - (size/branches) * i, 0);
            ctx01.rotate(-spread);
            ctx01.scale(scale, scale);
            drawBranch(level + 1);
            ctx01.restore();
        }
    }
    drawBranch(0);
    
    ctx01.restore();
});