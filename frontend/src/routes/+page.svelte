<script lang='ts'>
  import type { ConversationTarget, ConversationPlan } from '$lib/types';
  import { createStarLayers } from '$lib/loader';
  import '$lib/loader'
  import '$lib/loader.css';
  import Dashboard from '$lib/dashboard.svelte';
  let goal: string = '';
  let situation: string = '';
  let occupation: string = '';
  let relationship: string = '';
  let activity: string = '';
  let showDashboard: boolean = false;
  let isLoading: boolean = false;
  let dashboardData: { [key: string]: ConversationPlan } = {};
  let starLayers: any[] = createStarLayers(); //create stars for loader animation

  const endpoints = ['opening', 'topic', 'sustain', 'rapport', 'closing', 'joke', 'excuse'];

  async function fetchPlan(endpoint: string): Promise<ConversationPlan> {
    const response = await fetch(`https://khangta.dev/plan/${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        goal, 
        situation, 
        occupation,
        relationship,
        activity } as ConversationTarget)
    });

    if (response.ok) {
      return response.json() as Promise<ConversationPlan>;
    } else {
      throw new Error(`Error fetching data from ${endpoint}`);
    }
  }

  async function generate() {
    isLoading = true;
    try {
      const promises = endpoints.map(endpoint => fetchPlan(endpoint));
      const results = await Promise.all(promises);

      endpoints.forEach((endpoint, index) => {
        dashboardData[endpoint] = results[index];
      });

      // dashboardData['opening'] = await fetchPlan('opening'); // test

      showDashboard = true;
    } catch (error) {
      console.error('Failed to fetch plans:', error);
    } finally {
      isLoading = false;
    }
  }

  function toggleDashboard() {
    showDashboard = false;
  }

</script>

<body class="flex flex-col items-center justify-center bg-gray-200 text-gray-700 bg-cover bg-[url('https://images.pexels.com/photos/6115011/pexels-photo-6115011.jpeg')] animate-slidein">
  {#if !showDashboard}
  <div class="flex items-center justify-center absolute inset-0 bg-red-300 bg-opacity-30 rounded"> 
    <div class={`container ${isLoading ? 'opacity-25 blur' : ''} mx-auto p-4 flex flex-col w-screen h-screen items-center justify-center`}>
      <h1 class="font-bold text-5xl text-white">Conversational Repertoire</h1>
      <form on:submit|preventDefault={ generate } class="space-y-4 flex flex-col bg-white rounded shadow-lg w-[32rem] p-12 mt-12">
        <label class="font-semibold text-m" for="goal">The goal of the conversation</label>
        <input type="text" bind:value={goal} placeholder="What do you want to achieve?" class="flex items-center p-2 border border-gray-300 rounded-md shadow-sm w-full" />
        <label class="font-semibold text-m" for="situation">Your situation</label>
        <input type="text" bind:value={situation} placeholder="Where are you at? What occassion?" class="flex items-center p-2 border border-gray-300 rounded-md shadow-sm w-full" />
        <label class="font-semibold text-m" for="occupation">Their occupation</label>
        <input type="text" bind:value={occupation} placeholder="You can guess or type 'dont know'" class="flex items-center p-2 border border-gray-300 rounded-md shadow-sm w-full" />
        <label class="font-semibold text-m" for="relationship">Your relationship with them</label>
        <input type="text" bind:value={relationship} placeholder="Do you know them or just a stranger?" class="flex items-center p-2 border border-gray-300 rounded-md shadow-sm w-full" />
        <label class="font-semibold text-m" for="activity">Their activity</label>
        <input type="text" bind:value={activity} placeholder="What are they doing?" class="flex items-center p-2 border border-gray-300 rounded-md shadow-sm w-full" />
        <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md shadow hover:bg-blue-600">Make Plan</button>
      </form>
    </div>
  </div>
  {/if}
  
  {#if isLoading}
  <div class="loader flex flex-col items-center justify-center">
    <div id="circle_container">
      <div id="stars">
        {#each starLayers as { layerIndex, transform, stars }}
          <div class="star_layer" style="transform: {transform};">
            {#each stars as star}
              <div class="star" style="top: {star.top}; left: {star.left}; opacity: {star.opacity};"></div>
            {/each}
          </div>
        {/each}
      </div>
      <div id="load_wrapper">
        <div id="sun"></div>
        <div id="moon"></div>
      </div>
    </div>
    <h1 id="loading_text">Loading</h1>
  </div>
  {:else if showDashboard}
  <div class={`container ${showDashboard ? 'grid grid-rows-[auto,1fr,auto]' : 'hidden'} gap-4 mx-auto p-4 flex flex-col items-center justify-center`}>
    <div class="flex justify-center w-full">
      <label class="font-semibold text-5xl text-white" for="opening">From the start</label>
    </div>
    <div class="flex justify-between items-center gap-4 row-span-1">
      <Dashboard data={dashboardData.topic} />
      <Dashboard data={dashboardData.opening} />
    </div>
    <div class="flex justify-center w-full">
      <label class="font-semibold text-5xl text-white" for="middle">During the conversation</label>
    </div>
    <div class="flex justify-between items-center gap-4 row-span-1">
      <Dashboard data={dashboardData.sustain} />
      <Dashboard data={dashboardData.rapport} />
      <Dashboard data={dashboardData.joke} />
    </div>
    <div class="flex justify-center w-full">
      <label class="font-semibold text-5xl text-white" for="ending">Ending</label>
    </div>
    <div class="flex justify-between items-center gap-4 row-span-1">
      <Dashboard data={dashboardData.excuse} />
      <Dashboard data={dashboardData.closing} />
    </div>

    <button 
      class="px-4 py-2 bg-blue-500 text-white rounded-md shadow hover:bg-red-600 mt-4"
      on:click={toggleDashboard}>
      Start Again
    </button>
  </div>
  {/if}
</body>

<style>
@keyframes slidein {
from {
  background-position: top;
  background-size: 3000px;
}
to {
  background-position: -100px 0px;
  background-size: 2750px;
}
}

.animate-slidein {
  animation: slidein 100s infinite alternate forwards;
}
</style>



