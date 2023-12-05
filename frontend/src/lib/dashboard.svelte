<script lang="ts">
  import type { ConversationPlan } from '$lib/types';
  export let data: ConversationPlan | null;

</script>

{#if data} 
  <div class="box">
    <h2 class="text-lg font-semibold">{data.name}</h2>
    <p>{@html data.content}</p>
  </div>
{/if}

<style lang="postcss">
  .box {
    @apply flex-1 m-4 p-6 bg-gray-100 rounded-lg shadow-lg w-1/4;
    /* @apply flex-1 p-4 border border-gray-300 rounded-md shadow-sm; */
  }
</style>
