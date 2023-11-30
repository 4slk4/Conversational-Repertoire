// Function to generate random numbers
function getRandom(size: number) {
    return Math.floor(Math.random() * size);
  }

// Function to create star layers for the loader
export function createStarLayers() {
    return Array.from({ length: 10 }, (_, layerIndex) => ({
        layerIndex,
        transform: `translateZ(${layerIndex}px) scale(${(15 - layerIndex) / 15})`,
        stars: Array.from({ length: 7 }, () => ({
        top: getRandom(200) + 'px',
        left: getRandom(200) + 'px',
        opacity: (20 + getRandom(50)) / 100
        }))
    }));
}

