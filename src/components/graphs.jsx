import firstgraph from '/public/1gr.png';
import secondgraph from '/public/2gr.png';
import thirdgraph from '/public/3gr.png';
import fourthgraph from '/public/4gr.png';


function Graphs() {
    return (
     <div className='sm:max-lg:mt-40 grid grid-cols-1 gap-5 mx-auto mt-3 mb-5'>
        <div class="rounded-xl bg-white w-full"><img src={firstgraph}/></div>
        <div class="rounded-xl bg-white w-full"><img src={secondgraph}/></div>
        <div class="rounded-xl bg-white w-full"><img src={thirdgraph}/></div>
        <div class="rounded-xl bg-white w-full"><img src={fourthgraph}/></div>
      </div>
    );
  }

export default Graphs;