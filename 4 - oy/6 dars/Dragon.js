// const run = () => {
//     requestAnimationFrame(run); 
//     let e = elems[0];
    
//     const ax = (Math.cos(3 * frm) * rad * width) / height; 
//     const ay = (Math.sin(4 * frm) * rad * height) / width; 
    
//     e.x += (ax + pointer.x - e.x) / 10; 
//     e.y += (ay + pointer.y - e.y) / 10; 
    
//     for (let i = 1; i < N; i++) {
//         let e = elems[i]; 
//         let ep = elems[i - 1]; 
//         const a = Math.atan2(e.y - ep.y, e.x - ep.x); 
        
//         e.x += (ep.x - e.x + (Math.cos(a) * (100 - i)) / 5) / 4; 
//         e.y += (ep.y - e.y + (Math.sin(a) * (100 - i)) / 5) / 4; 
        
//         const s = (162 + 4 * (1 - i)) / 50; 
        
//         e.use.setAttribute('transform', 
//             `translate(${(ep.x + e.x) / 2}, ${(ep.y + e.y) / 2}) rotate(${(180 / Math.PI) * a}) translate(0, 0) scale(${s}, ${s})`
//         );
//     }
// };
