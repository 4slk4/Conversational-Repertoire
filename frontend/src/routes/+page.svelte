<script lang='ts'>
    import type { ConversationTarget, ConversationPlan } from '$lib/types';
    import Dashboard from '$lib/Dashboard.svelte';
    let goal: string = '';
    let situation: string = '';
    let occupation: string = '';
    let relationship: string = '';
    let activity: string = '';
    let showDashboard: boolean = false;
    let isLoading: boolean = false;
    let dashboardData: { [key: string]: ConversationPlan } = {};

    const endpoints = ['opening', 'topic', 'sustain', 'rapport', 'closing', 'joke', 'excuse'];

    async function fetchPlan(endpoint: string): Promise<ConversationPlan> {
      const response = await fetch(`http://localhost:8000/plan/${endpoint}`, {
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
</script>

<div class={`container ${isLoading ? 'opacity-25 blur' : ''} mx-auto p-4`}>
<form on:submit|preventDefault={ generate } class="space-y-4">
    <input type="text" bind:value={goal} placeholder="Goal of the conversation" class="p-2 border border-gray-300 rounded-md shadow-sm w-full" />
    <input type="text" bind:value={situation} placeholder="What is the situation?" class="p-2 border border-gray-300 rounded-md shadow-sm w-full" />
    <input type="text" bind:value={occupation} placeholder="What is that person's occupation based on their outfit? type 'don't know' if you don't know" class="p-2 border border-gray-300 rounded-md shadow-sm w-full" />
    <input type="text" bind:value={relationship} placeholder="What is your relationship with that person?" class="p-2 border border-gray-300 rounded-md shadow-sm w-full" />
    <input type="text" bind:value={activity} placeholder="What activity is that person doing?" class="p-2 border border-gray-300 rounded-md shadow-sm w-full" />
    <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md shadow hover:bg-blue-600">Generate</button>
</form>
</div>


{#if isLoading}
<div class="container mx-auto p-4">
  <div class="flex justify-center items-center">
    <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
  </div>
</div>
{:else if showDashboard}
<div class={`container ${showDashboard ? 'grid grid-rows-[auto,1fr,auto]' : 'hidden'} gap-4 mx-auto p-4`}>
  <div class="flex justify-between items-center gap-4 row-span-1">
    <Dashboard data={dashboardData.topic} />
    <Dashboard data={dashboardData.opening} />
  </div>
  
  <div class="flex justify-between items-center gap-4 row-span-1">
    <Dashboard data={dashboardData.sustain} />
    <Dashboard data={dashboardData.rapport} />
    <Dashboard data={dashboardData.joke} />
  </div>
  
  <div class="flex justify-between items-center gap-4 row-span-1">
    <Dashboard data={dashboardData.excuse} />
    <Dashboard data={dashboardData.closing} />
  </div>
</div>
{/if}



