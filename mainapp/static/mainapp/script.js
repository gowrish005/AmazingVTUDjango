       // Loader
       window.addEventListener('load', () => {
        document.querySelector('.loader').style.display = 'none';
    });

    // Particles.js Config
    particlesJS("particles-js", {
        particles: {
            number: { value: 80, density: { enable: true, value_area: 800 } },
            color: { value: "#ffffff" },
            shape: { type: "circle" },
            opacity: { value: 0.5, random: false },
            size: { value: 3, random: true },
            line_linked: {
                enable: true,
                distance: 150,
                color: "#ffffff",
                opacity: 0.4,
                width: 1
            },
            move: {
                enable: true,
                speed: 6,
                direction: "none",
                random: false,
                straight: false,
                out_mode: "out",
                bounce: false,
            }
        },
        interactivity: {
            detect_on: "canvas",
            events: {
                onhover: { enable: true, mode: "repulse" },
                onclick: { enable: true, mode: "push" },
                resize: true
            },
            modes: {
                repulse: { distance: 100, duration: 0.4 },
                push: { particles_nb: 4 }
            }
        },
        retina_detect: true
    });

    // Scroll Progress
    window.addEventListener('scroll', () => {
        const winScroll = document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        document.querySelector('.scroll-progress').style.height = scrolled + "%";
    });

    // Smooth Scroll
    document.querySelector('.scroll-btn').addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector('#programs');
        target.scrollIntoView({ behavior: 'smooth' });
    });

    // GSAP Animations
    gsap.registerPlugin(ScrollTrigger);

    // Header Animation
    gsap.from('header h1', {
        duration: 1.5,
        y: 100,
        opacity: 0,
        ease: 'power4.out'
    });

    // Program Cards Animation
    gsap.utils.toArray('.program').forEach((program, i) => {
        gsap.from(program, {
            scrollTrigger: {
                trigger: program,
                start: 'top bottom-=100',
                toggleActions: 'play none none reverse'
            },
            y: 100,
            opacity: 0,
            duration: 1,
            delay: i * 0.2,
            ease: 'power4.out'
        });
    });

    // Three.js Scene Setup
   // Three.js Scene Setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
const container = document.getElementById('canvas-container');

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x000000, 0);
container.appendChild(renderer.domElement);

// Create text geometry
const loader = new THREE.FontLoader();
const textMesh = new THREE.Mesh();
const textMaterial = new THREE.MeshPhongMaterial({
color: 0xffffff,
specular: 0x666666
});

loader.load('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/fonts/helvetiker_regular.typeface.json', function(font) {
const textGeometry = new THREE.TextGeometry('Web Lab', {
    font: font,
    size: 3,
    height: 0.5,
    curveSegments: 12,
    bevelEnabled: true,
    bevelThickness: 0.1,
    bevelSize: 0.05,
    bevelOffset: 0,
    bevelSegments: 5
});

textGeometry.center();
textMesh.geometry = textGeometry;
textMesh.material = textMaterial;
scene.add(textMesh);
});

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const pointLight = new THREE.PointLight(0xffffff, 1);
pointLight.position.set(5, 5, 5);
scene.add(pointLight);

camera.position.z = 15;

// Animation
function animate() {
requestAnimationFrame(animate);

if (textMesh) {
    textMesh.rotation.y += 0.005;
    textMesh.rotation.x = Math.sin(Date.now() * 0.001) * 0.1;
}

renderer.render(scene, camera);
}

// Handle window resize
window.addEventListener('resize', () => {
const width = window.innerWidth;
const height = window.innerHeight;

camera.aspect = width / height;
camera.updateProjectionMatrix();
renderer.setSize(width, height);
});

// Initialize animation
animate();

// Additional GSAP Animations
// Program Cards Stagger Animation
// GSAP Animations
gsap.registerPlugin(ScrollTrigger);

// Header Animation
gsap.from('header h1', {
duration: 1.5,
y: 50,
opacity: 0,
ease: 'power4.out'
});

// Program Cards Animation with reduced movement
gsap.utils.toArray('.program').forEach((program, i) => {
gsap.from(program, {
    scrollTrigger: {
        trigger: program,
        start: 'top bottom-=100',
        toggleActions: 'play none none none'
    },
    y: 30,
    opacity: 0.8,
    duration: 0.8,
    delay: i * 0.1,
    ease: 'power2.out'
});
});

// Contact Form Animation
gsap.from('.cyber-border', {
scrollTrigger: {
    trigger: 'form',
    start: 'top bottom-=100',
    toggleActions: 'play none none none'
},
scale: 0.95,
opacity: 0.8,
duration: 0.8,
ease: 'power2.out'
});

// Footer Links Animation
gsap.from('footer a', {
scrollTrigger: {
    trigger: 'footer',
    start: 'top bottom-=50',
    toggleActions: 'play none none none'
},
y: 20,
opacity: 0.8,
duration: 0.8,
stagger: 0.1,
ease: 'power2.out'
});