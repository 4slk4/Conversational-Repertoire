<script>
    import Dashboard from '$lib/Dashboard.svelte';
    let goal = '';
    let context = '';
    let personality = '';
    let showDashboard = false;
  
    function generate() {
      showDashboard = true;
    }
</script>

<div class={`container ${showDashboard ? 'opacity-25 blur' : ''} mx-auto p-4`}>
<form on:submit|preventDefault={generate} class="space-y-4">
    <input type="text" bind:value={goal} placeholder="Goal of the conversation" class="p-2 border border-gray-300 rounded-md shadow-sm w-full" />
    <input type="text" bind:value={context} placeholder="Context" class="p-2 border border-gray-300 rounded-md shadow-sm w-full" />
    <input type="text" bind:value={personality} placeholder="Personality" class="p-2 border border-gray-300 rounded-md shadow-sm w-full" />
    <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md shadow hover:bg-blue-600">Generate</button>
</form>
</div>

{#if showDashboard}
    <Dashboard show={showDashboard} />
{/if}

