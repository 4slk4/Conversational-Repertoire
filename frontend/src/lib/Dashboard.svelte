<script>
    export let show = false;
  </script>
  
  <div class={`fixed inset-0 bg-white bg-opacity-75 z-10 flex justify-center items-center transition-opacity duration-300 ${show ? 'opacity-100' : 'opacity-0 pointer-events-none'}`}>
    <div class="box">...</div>
    <div class="box">...</div>
    <div class="box">...</div>
  </div>
  
  <style lang="postcss">
    .box {
      @apply m-4 p-6 bg-gray-100 rounded-lg shadow-lg w-1/4;
    }
  </style>
  