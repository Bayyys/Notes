import { getImageUrl } from "../utils/utils.js";

function Card({ name, imgUrl, profession, awards, discovered }) {
  return (
    <>
      <section className="profile">
        <h2 className=" text-2xl font-semibold">{name}</h2>
        <img
          className="avatar"
          src={getImageUrl(imgUrl.getFrom)}
          alt={imgUrl.altFrom}
          width={70}
          height={70}
        />
        <ul>
          <li>
            <b>Profession: </b>
            {profession}
          </li>
          <li>
            <b>Awards: {awards.length} </b>(
            {awards.map((award, index) => {
              if (index === awards.length - 1) {
                return <span key={index}>{award}</span>;
              } else return <span key={index}>{award}, </span>;
            })}
            )
          </li>
          <li>
            <b>Discovered: </b>
            {discovered}
          </li>
        </ul>
      </section>
    </>
  );
}

export default function PropsTrans() {
  return (
    <div>
      <h1 className="text-2xl font-bold">Notable Scientists</h1>
      <Card
        name="Maria Skłodowska-Curie"
        imgUrl={{ getFrom: "szV5sdG", altFrom: "Maria Skłodowska-Curie" }}
        profession="physicist and chemist"
        awards={[
          "Nobel Prize in Physics",
          "Nobel Prize in Chemistry",
          "Davy Medal",
          "Matteucci Medal",
        ]}
        discovered="polonium (chemical element)"
      />
      <Card
        name="Katsuko Saruhashi"
        imgUrl={{ getFrom: "YfeOqp2", altFrom: "Katsuko Saruhashi" }}
        profession="geochemist"
        awards={["Miyake Prize for geochemistry", "Tanaka Prize"]}
        discovered="a method for measuring carbon dioxide in seawater"
      />
    </div>
  );
}
