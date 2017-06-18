(function exe(canv){
  const cx = canv.getContext("2d");
  const inputs = document.querySelectorAll("input");
  const m = inputs[0];
  const x = inputs[1];
  const b = inputs[2];
  const sub = inputs[3];

  window.addEventListener("load",()=>{
    let w = window.innerWidth;
    canv.width = canv.height = Math.round(w/3);
    graph();
  });

  window.addEventListener("resize",()=>{
    let w = window.innerWidth;
    canv.width = canv.height = Math.round(w/3);
    graph();
  });

  sub.addEventListener("click",e =>{
    let rate = +m.value;
    let variable = +x.value;
    let initial = +b.value;
    let expression = linear(rate,variable,initial);
    graph(expression);
  });

  //returns linear expression
  function linear(r,x,b){
    if(!!r && !!x && !!b)
      return String(r*x + b);
    else if(r === 0 && x === 0 && b === 0)
      return "x";

    if(!!r && !!x) return String(r*x);
    if(!!r && !!b) return r + "x+" + b;
    if(!!x && !!b) return String(x + b);

    if(!!r) return r + "x";
    if(!!x) return x;
    if(!!b) return "x+" + b;
  }

  function graph(exp){
    /*
      1. decide the scale of the graph,
    */
    //presets
    let center = canv.width/2;
    let length = canv.width;
    cx.strokeStyle = "#ddd";
    cx.fillStyle = "#000";
    cx.lineWidth = 2;

    //clear current graph
    cx.clearRect(0,0,length,length);
    cx.fillRect(0,0,length,length);

    //axes
    cx.beginPath();cx.moveTo(center, 0);cx.lineTo(center, length);
    cx.moveTo(0,center);cx.lineTo(length,center);cx.stroke();

    if(typeof exp === "undefined") return;
    //parse the expression
    let m = isNaN(exp) ? _parse(exp).m : 0;
    let b = isNaN(exp) ? _parse(exp).b : +exp;

    function _parse(exp){
      let arr = exp.split("");
      let ignore = false;

      let m = arr.reduce((acc, val)=>{
        if(val === "x") ignore = !ignore;
        if(!ignore) return acc+=val;
        return acc;
      },"");

      ignore = true;
      let b = arr.reduce((acc,val)=>{
        if(!ignore) return acc+=val;
        if(val === "+") ignore = !ignore;
        return acc;
      },"");
      return {
        m:m,
        b:b
      };
    }

    //compare slope and initial value to length of the canvas, normalize it to 1/100
    let valuePerUnit = Math.max(m,b)/100;

  }

})(document.querySelector("canvas"));
