export default function Typography() {
  return (
    <div className="space-y-4">
      <h1 className="text-red-600 text-3xl">标题1</h1>
      <h2 className="font-sans hover:font-serif md:font-mono">
        Fonrfamilt: serif
      </h2>
      <p className="not-italic hover:italic">Lorem ipsum dolor sit amet.</p>
      <ul>
        <li className="text-xs">text-xs</li>
        <li className="text-lg">text-lg</li>
        <li className="text-3xl">text-3xl</li>
        <li className="text-xl">text-xl</li>
        <li className="text-xl/8">text-xl/8</li>
        <li className="font-thin">font-thin</li>
        <li className="font-black">font-black</li>
        <li className="tracking-tighter">tracking-tighter</li>
        <li className="tracking-widest">tracking-widest</li>
      </ul>
      <p className="line-clamp-2">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt
        possimus facilis sed distinctio sunt cum repellendus, exercitationem
        culpa modi. Voluptatum nisi sunt vel quidem, fuga voluptatem suscipit
        iste unde dolore.
      </p>
      <ul>
        <li className="leading-3">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi
          perferendis, quo, eveniet odio sapiente commodi sint voluptate quia
          doloribus veniam ratione, dolores nostrum est. Molestias modi animi
          atque ex nihil.
        </li>
        <li className="leading-10 text-center">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Saepe
          architecto, excepturi unde iste ea est temporibus assumenda sunt
          aliquam, tenetur obcaecati beatae debitis quibusdam ipsum, molestiae
          perspiciatis minus cupiditate. Praesentium!
        </li>
      </ul>
      <ul className="list-inside list-decimal">
        <li>Lorem, ipsum dolor.</li>
        <li>Vel, ipsum blanditiis!</li>
        <li>Distinctio, pariatur eveniet.</li>
      </ul>
      <hr />
      <h1>文本颜色</h1>
      <h2 className="text-blue-600 hover:text-blue-600/50">text-blue-600/50</h2>
      <hr />
      <h1>文本修饰</h1>
      <h2 className="text-xl underline">underline</h2>
      <h2 className="text-xl overline">overline</h2>
      <h2 className="text-xl line-through">line-through</h2>
      <h2 className="decoration-blue-500 hover:decoration-red-500/50 line-through">
        decoration-blue-50
      </h2>
      <h2 className="underline decoration-double decoration-4">
        devoration-double
      </h2>
      <h2 className="underline decoration-double decoration-2 underline-offset-2">
        devoration-double
      </h2>
      <hr />
      <h1>文本转换</h1>
      <h2 className="uppercase">uppercase</h2>
      <h2 className=" capitalize hover:lowercase">capitalize</h2>
      <hr />
      <h1>文本溢出</h1>
      <p className=" text-ellipsis overflow-hidden...">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maiores ex
        maxime delectus non dolores quidem blanditiis, exercitationem
        consectetur ducimus veniam voluptatem alias expedita error beatae odio
        iste suscipit fugiat laboriosam.
      </p>
      <p className="indent-4">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis aliquid
        quaerat enim laboriosam exercitationem debitis sequi fuga expedita,
        labore id non eveniet quia saepe unde error adipisci possimus harum
        voluptatem quidem, dolorem nisi cupiditate? Excepturi exercitationem
        natus fuga officia ea quae minus voluptatum ut sit tempore asperiores
        sapiente soluta odit ad, minima tempora ipsam iusto facere nesciunt.
        Tempora sint quisquam minus suscipit facere molestias animi dicta. Quod
        dolores qui, pariatur rerum suscipit quis aspernatur, quo fugiat
        exercitationem nisi architecto perferendis. Aliquid quis doloribus
        pariatur asperiores unde voluptatem autem, quae, excepturi non labore
        delectus culpa sequi. Fugit voluptate voluptas rem atque?
      </p>
      <p className=" align-baseline">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Harum maiores
        ea eveniet illo recusandae voluptate? Dolore nobis doloremque officia
        ipsum quod! Ea, eos maiores. Aut quas commodi maxime nulla quia?
      </p>
      <hr />
      <h1>内容</h1>
      <p>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. In similique
        mollitia vero accusamus quia minima vel perspiciatis corporis, tempore
        nobis nisi autem odit.<a className="after:content-['↑']">测试</a> Beatae
        nobis eaque molestiae aliquid tempore error?
      </p>
    </div>
  );
}
